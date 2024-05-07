from algokit_utils.beta.algorand_client import(
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams
)

algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
# print("dispenser adx",dispenser.address)
creator = algorand.account.random()
# print("creator adx: ",creator.address)
algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)
# print("funded creator: \n",algorand.account.get_information(creator.address))
# reciever1 =algorand

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=1000,
        asset_name="MyAlgo",
        unit_name="MALG"
    )
)
asset_id = sent_txn["confirmation"]["asset-index"]
# print ("asset ID: ", asset_id)

rec_1 = algorand.account.random() 
rec_2 = algorand.account.random()
rec_3 = algorand.account.random()
print("R1:", rec_1.address,"R2:", rec_2.address,"R3:", rec_3.address )

algorand.send.payment(
        PayParams(
        sender=dispenser.address,
        receiver=rec_1.address,
        amount=10_000_000
    )
)
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=rec_1.address,
        asset_id=asset_id
    )
)


asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=rec_1.address,
        asset_id=asset_id,
        amount=100   
    )
)
print("For Rec 1: \n",algorand.account.get_information(rec_1.address))

algorand.send.payment(
        PayParams(
        sender=dispenser.address,
        receiver=rec_2.address,
        amount=10_000_000
    )
)
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=rec_2.address,
        asset_id=asset_id
    )
)


asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=rec_2.address,
        asset_id=asset_id,
        amount=100,
        last_valid_round=1000   
    )
)
print("For Rec 2: \n",algorand.account.get_information(rec_2.address))

algorand.send.payment(
        PayParams(
        sender=dispenser.address,
        receiver=rec_3.address,
        amount=10_000_000
    )
)
algorand.send.asset_opt_in(
    AssetOptInParams(
        sender=rec_3.address,
        asset_id=asset_id
    )
)


asset_transfer = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=rec_3.address,
        asset_id=asset_id,
        amount=100,
        last_valid_round=1000   
    )
)
print("For Rec 3: \n",algorand.account.get_information(rec_3.address))
print("For Creator: \n",algorand.account.get_information(creator.address))