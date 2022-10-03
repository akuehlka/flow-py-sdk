# %%
import asyncio
from flow_py_sdk import *

async def gettx(tx):
    async with flow_client(
        host='access-001.mainnet19.nodes.onflow.org', port=9000
    ) as client:
        txdata = await client.get_transaction(id=bytes.fromhex(tx))
        return txdata

async def gettxres(tx):
    async with flow_client(
        host='access-001.mainnet19.nodes.onflow.org', port=9000
    ) as client:
        txresdata = await client.get_transaction_result(id=bytes.fromhex(tx))
        return txresdata

async def getblock(height):
    async with flow_client(
        host='access-001.mainnet19.nodes.onflow.org', port=9000
    ) as client:
        blockdata = await client.get_block_by_height(height=height)
        return blockdata

async def getevts(blockid):
    async with flow_client(
        host='access-001.mainnet19.nodes.onflow.org', port=9000
    ) as client:
        evtdata = await client.get_events_for_block_i_ds(type='FlowFees.FeesDeducted', block_ids=[blockid])
        return evtdata

#%%
txresult = asyncio.run(gettxres('219c8a39b0291987ffa2061d6784feafd4b32652d753daacdbb6fba3bb7e0880'))
for e in txresult.events:
    print(e)

# %%
