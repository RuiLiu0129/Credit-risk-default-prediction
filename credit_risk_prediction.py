
import matplotlib.pyplot as plt
import seaborn as sns



path="~/Desktop/2019 Spring/Advanced Big Data Analysis/my project/credit/home-credit-default-risk/"

app_test = pd.read_csv(path+"application_test.csv")
app_train = pd.read_csv(path+"application_train.csv")
bureau = pd.read_csv(path+"bureau.csv")
credit_card_balance = pd.read_csv(path+"credit_card_balance.csv")
installments_payments = pd.read_csv(path+"installments_payments.csv")
POS_CASH_balance = pd.read_csv(path+"POS_CASH_balance.csv")
previous_application = pd.read_csv(path+"previous_application.csv")


