URL = 'https://erp.ncuindia.edu/'

UNAME_ID = 'tbUserName'
PASS_ID  = 'tbPassword'

N_MON = 15
N_TUE = 16
N_WED = 15
N_THU = 16
N_FRI = 15

MON = ("AI", "CC", "ES", "SE", "ES")
TUE = ("AI", "ES", "SE", "CC")
WED = ("IS&C", "AI", "CTC")
THU = ("ES", "IS&C", "SE", "SE")
FRI = ("CC", "IS&C", "IS&C", "ES")

SUBJECTS = ["AI", "SE", "ES", "IS&C", "CC", "CTC"]

N_ATTRIBUTES = 3
ATTRIBUTES   = ["Total", "Present", "Absent"]

total = {
    "AI" : [0, 0, 0], "SE" : [0, 0, 0], "ES" : [0, 0, 0],
    "IS&C" : [0, 0, 0], "CC" : [0, 0, 0], "CTC" : [0, 0, 0]
}

THRESHOLD = 0.25