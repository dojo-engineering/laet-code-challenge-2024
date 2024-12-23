class Payment:
    def __init__(self, id, amount, date, method, status):
        self.amount = amount
        self.id = id
        self.date = date
        self.method = method
        self.status = status

payments_data = [
    Payment("ca6e6c66-11c4-5108-b9c0-fea33d683231", 45, "2024-11-25", "Visa", "Failed"),
    Payment("4e06e95a-dbbe-5275-b6be-c8bc94d6dfb9", 23, "2024-11-26", "Mastercard", "Success"),
    Payment("3d57beca-cb73-583b-a39b-f7f4777cd604", 12, "2024-11-29", "Visa", "Success"),
    Payment("85aebc6b-c6e4-59bc-9e62-90cebc611134", 67, "2024-11-27", "Amex", "Success"),
    Payment("86a9ad9f-becd-56df-adc3-bc4061229523", 89, "2024-11-28", "Paypal", "Failed"),
    Payment("60beb2d6-80b6-584b-9387-19941ccd0784", 34, "2024-11-30", "Mastercard", "Refunded"),
    Payment("80779444-4f69-5492-a931-07a84e5e358a", 56, "2024-11-01", "Amex", "Failed"),
    Payment("bb6d750a-3e16-5193-bca8-b4edf3e41308", 22, "2024-11-05", "Amex", "Success"),
    Payment("56776912-e67f-55e3-b831-b835fb0fe1b4", 78, "2024-11-02", "Paypal", "Success"),
    Payment("4762572f-1945-52bc-a691-023da0a84d5b", 90, "2024-11-03", "Visa", "Failed"),
    Payment("868a0bc3-dd2b-58a5-9012-297937e2a67c", 11, "2024-11-04", "Mastercard", "Success"),
    Payment("6087e293-529e-5ce5-bc1a-befff30ed7d6", 33, "2024-11-06", "Paypal", "Failed"),
    Payment("3e9dd7f0-9e52-5e66-86f6-d702be77d0e0", 44, "2024-11-07", "Visa", "Success"),
    Payment("a7d17d23-29e0-5ad4-a501-3c6fdc265df1", 99, "2024-11-12", "Mastercard", "Success"),
    Payment("0b49ce8c-e90f-55ef-936d-6c4f4d8d1327", 55, "2024-11-08", "Mastercard", "Success"),
    Payment("8f1de6f2-63c2-583e-9d0e-c893582d5ec3", 66, "2024-11-09", "Amex", "Failed"),
    Payment("3ef3297a-b007-53e0-9aab-430bc8361c57", 77, "2024-11-10", "Paypal", "Success"),
    Payment("2a7edcf8-8b01-5cae-bd19-71f3df3548d3", 88, "2024-11-11", "Visa", "Failed"),
    Payment("fe4bef56-9226-5d6b-a4ae-25b42ad6efa0", 10, "2024-11-13", "Amex", "Success"),
    Payment("9a1991ed-040e-546e-874f-14793d3d536d", 98, "2024-11-21", "Amex", "Success"),
    Payment("0f72cdf4-1cf7-5836-8c4b-d4f7881e3857", 21, "2024-11-14", "Paypal", "Failed"),
    Payment("b63c92a9-91bf-55e2-b7c0-9b75f6d47a15", 43, "2024-11-16", "Mastercard", "Success"),
    Payment("3253ed0e-0660-5718-b579-ee624f8c69d4", 32, "2024-11-15", "Visa", "Success"),
    Payment("e712765c-d6e4-5872-a6f5-7120572f8006", 65, "2024-11-18", "Paypal", "Success"),
    Payment("eabe37e3-3173-597f-a3fe-ac569e527e3e", 54, "2024-11-17", "Amex", "Failed"),
    Payment("b3682f7c-8cbd-55a9-ba93-26844ba848fd", 87, "2024-11-20", "Mastercard", "Success"),
    Payment("9c791fb7-58cb-5e1d-bb81-3614dde4406d", 19, "2024-11-22", "Paypal", "Failed"),
    Payment("a228a82c-5894-56bd-8641-a8d0f57d3533", 30, "2024-11-23", "Visa", "Success"),
    Payment("dc005a8f-2b94-5d81-8c4b-c56a806c5eb2", 41, "2024-11-24", "Mastercard", "Success"),
    Payment("ddbb1330-f5b4-5de5-ac7c-aaac84c81773", 52, "2024-11-25", "Amex", "Failed"),
    Payment("cc58c702-58cb-5c0f-ba70-58df1ddb89dc", 76, "2024-11-19", "Visa", "Failed"),
    Payment("518a687a-ed98-5846-8af6-bdfea3058b3e", 63, "2024-11-26", "Paypal", "Success"),
    Payment("250e4b1d-7337-5020-9bb5-4b33faa7131f", 96, "2024-11-29", "Amex", "Success"),
    Payment("b3b81343-45c2-5ce7-9c51-fa3663ee52d5", 85, "2024-11-28", "Mastercard", "Success"),
    Payment("a72099b9-ee2e-5e55-a3ef-c45994246130", 17, "2024-11-30", "Paypal", "Failed"),
    Payment("f1a5b962-da98-58ac-adb4-be1edd44d5f6", 28, "2024-11-30", "Visa", "Success"),
    Payment("7ba7a509-4278-5fff-a4aa-b7e9cd5c5eb3", 39, "2024-11-25", "Mastercard", "Success"),
    Payment("6fd1d933-e717-5beb-bb56-21586cf03754", 74, "2024-11-27", "Visa", "Failed"),
    Payment("9c106bf6-af00-54cf-8d4c-7fffd5ab983a", 50, "2024-11-26", "Amex", "Failed"),
    Payment("732a880b-d7b2-5156-a698-765611a0aea0", 61, "2024-11-27", "Paypal", "Success"),
    Payment("af3855a2-2dfb-54ee-8dfa-e1535098cbb7", 83, "2024-11-29", "Mastercard", "Success"),
    Payment("d3a4e812-4f43-5b88-ad6c-a6de6ad3cf58", 72, "2024-11-28", "Visa", "Failed"),
    Payment("3bcb609f-e6a8-5c87-b87d-5d21d163602d", 70, "2024-11-06", "Visa", "Failed"),
    Payment("e5bb81c6-7bfd-5d14-9953-735e42d3ea29", 48, "2024-11-04", "Amex", "Failed"),
    Payment("ce9548d9-b1f9-5d34-9796-9a60f95dd20f", 81, "2024-12-10", "Mastercard", "Success"),
    Payment("412c0b0a-cc66-5e08-bcca-54e18ac43e54", 44, "2024-11-20", "Amex", "Failed"),
    Payment("138024c5-5b0d-5a00-8fa3-f9b72417433f", 55, "2024-12-09", "Paypal", "Refunded"),
    Payment("a8f88f77-ed72-5de7-b590-36ae8aed371c", 43, "2024-11-29", "Paypal", "Success"),
    Payment("3915b505-d4f0-544a-a3ea-a6806a91a007", 66, "2024-12-09", "Visa", "Failed"),
    Payment("06c28045-a54b-51eb-bbb4-040113c5e17d", 88, "2024-11-24", "Amex", "Success"),
    Payment("4df4ec4e-ec90-596c-b013-6cf26e85dcfc", 37, "2024-11-03", "Mastercard", "Success"),
    Payment("d442ecea-347f-59ff-ba81-553eff3cd9ae", 94, "2024-12-10", "Amex", "Success"),
    Payment("0bddd94f-99f1-51db-a475-0dd01ed0e1f1", 24, "2024-12-10", "Visa", "Success"),
    Payment("ede7bf3a-dbbc-5f9a-8481-1312386c42b3", 35, "2024-12-06", "Mastercard", "Success"),
    Payment("9416d0a0-7d8c-5897-87bd-2fc36caf8a7a", 26, "2024-12-02", "Visa", "Success"),
    Payment("c82593d7-a253-5166-9bb7-7de5bf353052", 57, "2024-12-10", "Paypal", "Success"),
    Payment("78249616-b128-504e-bc59-ea3c623b9f42", 46, "2024-11-12", "Amex", "Failed"),
    Payment("5279cb0d-a30f-54e9-85cf-cfbf01bb3be8", 68, "2024-11-14", "Visa", "Refunded"),
    Payment("b71cc6b9-4b1d-5363-b531-10d5b70a16e1", 11, "2024-11-17", "Paypal", "Failed"),
    Payment("a0307d09-c137-5e94-a3aa-29fad81d0366", 79, "2024-11-15", "Mastercard", "Success"),
    Payment("f4fe0249-a23b-59c5-b7e3-36fd1572de72", 90, "2024-11-16", "Amex", "Success"),
    Payment("cd2132fc-2230-5f57-a182-dcf691f92c75", 15, "2024-11-01", "Paypal", "Failed"),
    Payment("d2feede0-f518-5709-b812-22133ae2e9da", 10, "2024-11-26", "Visa", "Success"),
    Payment("1587581a-98c8-5eab-9acd-4eec456eb67f", 32, "2024-11-28", "Amex", "Failed"),
    Payment("285a31f0-41ec-5d96-ad3f-9808b32e8d09", 59, "2024-11-05", "Paypal", "Success"),
    Payment("fe9c676e-674e-5808-8a26-9181e4622cc4", 13, "2024-11-09", "Paypal", "Failed"),
    Payment("d6a73ef8-43b1-5c0b-ad62-1cdc2a2c7a35", 33, "2024-11-19", "Mastercard", "Success"),
    Payment("2b910b6e-a6a5-5417-9826-7f04c794a11d", 22, "2024-11-18", "Visa", "Success"),
    Payment("ceca3d22-1365-588f-916c-ca04b7906eaa", 92, "2024-12-08", "Amex", "Success"),
    Payment("68464519-7ade-52e6-acfc-eda9bb6177a2", 77, "2024-11-23", "Mastercard", "Success"),
    Payment("dd5ce719-f139-5a29-a285-6cb8a09121e2", 99, "2024-11-25", "Paypal", "Failed"),
    Payment("aa0aeadf-ec37-587c-af8a-908ed40a93c0", 54, "2024-11-30", "Visa", "Failed"),
    Payment("3e3a5381-b684-545a-9256-ac8049958ccb", 65, "2024-11-29", "Mastercard", "Success"),
    Payment("9021b974-c23b-57f9-a231-6cac644d5ae7", 21, "2024-11-27", "Mastercard", "Success"),
    Payment("0d9ee55f-56da-5dbd-b6e2-5d08f59e3be0", 52, "2024-12-01", "Visa", "Failed"),
    Payment("3e9abd36-355d-569d-b4e6-1390fd767293", 76, "2024-11-25", "Amex", "Success"),
    Payment("37509ff5-3d1c-5a5c-9802-8c4c1ed22a1e", 96, "2024-12-05", "Visa", "Success"),
    Payment("7c78c658-11f8-57ac-9b02-ae8976a86eac", 74, "2024-12-03", "Amex", "Refunded"),
    Payment("fdac8d97-ba88-56df-9cee-9a4d68f50f43", 85, "2024-12-04", "Paypal", "Failed"),
    Payment("02b3fa20-a1c2-519c-9c7c-182a49c4e5dd", 63, "2024-12-02", "Mastercard", "Success"),
    Payment("a2efb157-225c-5152-a31a-e6f9cc431ed1", 28, "2024-12-07", "Amex", "Failed"),
    Payment("5cd3a479-9829-5958-950c-d3e95df4003a", 17, "2024-12-06", "Mastercard", "Success"),
    Payment("f2220136-2473-5c24-a6a0-e12018094558", 39, "2024-12-08", "Paypal", "Refunded"),
    Payment("ad67131f-f4d2-5719-a87a-abaf2dfadc3c", 61, "2024-12-10", "Mastercard", "Success"),
    Payment("2b2161c8-a038-5519-a54a-d078422c317c", 50, "2024-12-09", "Visa", "Failed"),
    Payment("fc59ace7-c659-5954-8771-86b839de5692", 72, "2024-12-11", "Amex", "Success"),
    Payment("fc59ace7-c659-5954-8771-86b839de5692", 72, "2024-12-11", "Visa", "Success"),
    Payment("fc59ace7-c659-5954-8771-86b839de5692", 72, "2024-12-11", "Mastercard", "Failed"),
    Payment("fc59ace7-c659-5954-8771-86b839de5692", 72, "2024-12-11", "Paypal", "Refunded"),
]