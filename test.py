from template_maker import entity_maker, da_maker



entity_maker("send",["product","quantity","customer",
                     "phone_number","address"])
da_maker("warehouse",["product","inventory"])
da_maker("send",["product","quantity","customer",
                     "phone_number","address"])
