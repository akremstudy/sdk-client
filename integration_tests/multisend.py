""" done
import lcd_auth
import lcd_authz
import lcd_bank
import lcd_distribution
import lcd_gov
import lcd_mint
import lcd_slashing
import lcd_wasm
import lcd_tendermint
import lcd_ibc
import lcd_ibc_transfer

"""

from sdk.client.lcd import LCDClient

# import lcd_tx
from sdk.client.lcd.api.tx import CreateTxOptions
from sdk.client.localterra import LocalTerra
from sdk.core.bank import MsgMultiSend, MsgSend, MultiSendInput, MultiSendOutput
from sdk.core.tx import SignMode
from sdk.key.mnemonic import MnemonicKey
from sdk.util.json import JSONSerializable

""" untested
import lcd_gov
"""

########

from sdk.core import Coin, Coins
from sdk.core.public_key import SimplePublicKey


def main():
    terra = LCDClient(
        url="https://pisco-lcd.terra.dev/",
        chain_id="pisco-1",
    )
    terra = LocalTerra()

    # key = MnemonicKey(
    #     mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    # )
    # test1 = terra.wallet(key=key)
    test1 = terra.wallets["test1"]

    msg = MsgSend(
        "terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(uluna=30000),
    )
    inputs = [
        MultiSendInput(
            address="terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
            coins=Coins(uluna=30000),
        )
    ]
    outputs = [
        MultiSendOutput(
            address="terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
            coins=Coins(uluna=10000),
        ),
        MultiSendOutput(
            address="terra1av6ssz7k4xpc5nsjj2884nugakpp874ae0krx7",
            coins=Coins(uluna=20000),
        ),
    ]
    msgMulti = MsgMultiSend(inputs, outputs)

    opt = CreateTxOptions(
        msgs=[msg, msgMulti], memo="send test", gas_adjustment=1.5, gas_prices="1uluna"
    )
    # tx = test1.create_tx(opt)
    tx = test1.create_and_sign_tx(opt)
    print("SIGNED TX", tx)

    result = terra.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
