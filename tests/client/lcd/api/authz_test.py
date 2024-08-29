from sdk.client.lcd import LCDClient, PaginationOptions

terra = LCDClient(
    url="https://pisco-lcd.terra.dev/",
    chain_id="pisco-1",
)


def test_grants():
    result = terra.authz.grants(
        "terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    )
    assert len(result) == 0

    result = terra.authz.granter("terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")
    assert len(result) == 2

    result = terra.authz.grantee("terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")

    assert len(result) == 1
