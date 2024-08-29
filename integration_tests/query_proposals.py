from sdk.client.lcd import LCDClient, PaginationOptions
from sdk.client.lcd.api.gov import ProposalStatus

terra = LCDClient(
    url="https://pisco-lcd.terra.dev/",
    chain_id="pisco-1",
)


result, pagination = terra.gov.proposals()

while pagination["next_key"] is not None:
    pagOpt = PaginationOptions(key=pagination["next_key"])
    result, pagination = terra.gov.proposals(params=pagOpt)
    pagOpt.key = pagination["next_key"]
    print(result)


result, pagination = terra.gov.proposals(
    options={
        "proposal_status": ProposalStatus.PROPOSAL_STATUS_DEPOSIT_PERIOD,
        "depositor": "terra1w8wc2ke09242v7vjqd5frzw6ulpz4l7yrcwppt",
    }
)
print(result)
