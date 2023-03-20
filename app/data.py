# import pandas as pd
# from faker import Faker
# from collections import defaultdict
# from sqlalchemy import create_engine

# fake = Faker()
# fake_data = defaultdict(list)

# for n in range(1000 ):
#     fake_data["id"].append( fake.random_number(digits=5) )
#     fake_data["username"].append( fake.first_name() )
#     fake_data["email_address"].append( fake.address() )
#     fake_data["age"].append( fake.pyint(2) )
#     fake_data["password_hash"].append( fake.password() )
#     fake_data["password1"].append( fake.password() )
#     fake_data["budget"].append( fake.randomize_nb_elements(number=100, ge=True, min=120))
#     fake_data["items"].append( fake.randomize_nb_elements(number=20) )

# df_fake_data = pd.DataFrame(fake_data)

# engine = create_engine('mysql://root:12345678@localhost/testdb', echo=False)

# df_fake_data.to_sql('usertable', con=engine,index=False)

