import asyncio
import base64
from pathlib import Path

import uvloop

from sdk.client.lcd import AsyncLCDClient
from sdk.core import Coins
from sdk.core.bank import MsgSend
from sdk.util.contract import get_code_id


async def main():
    terra = AsyncLCDClient(
        url="https://pisco-lcd.terra.dev/",
        chain_id="pisco-1",
    )

    result = await terra.tx.tx_infos_by_height(None)
    print(result)


uvloop.install()
asyncio.run(main())
