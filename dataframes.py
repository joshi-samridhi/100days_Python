#  Working pn Pandas
#  Install pandas by giving command in terminal 'pip install panndas'

emp_details={'emp_ID': [93,109,111],
              'emp_name': ['Sam', 'Radhika', 'Sushma'],
            'emp_desig': ['Sr.Sales Mgr','Lead Auditor','Server Admin']}

import pandas as pd
print(pd.DataFrame(emp_details))