import asyncio
import base64
from pathlib import Path

from sdk.client.lcd import LCDClient
from sdk.core import Coins
from sdk.core.bank import MsgSend
from sdk.util.contract import get_code_id


def main():
    terra = LCDClient(
        url="https://pisco-lcd.terra.dev/",
        chain_id="pisco-1",
    )

    result = terra.tx.tx_infos_by_height(None)
    print(result)


main()
