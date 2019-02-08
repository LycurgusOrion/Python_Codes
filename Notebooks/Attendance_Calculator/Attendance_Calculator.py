# Computational Libraries
from pandas import DataFrame
from matplotlib.pyplot import subplots
from numpy import array, floor 
from six import iteritems
# For sleep method
from time import sleep, perf_counter
# Configuration File
import config
# Selenium (for fetching data)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# # Attendance Viewer  and Calculator

# ### Importing Libraries

# DataFrame to Table Converting Function
def render_mpl_table(data, col_width=3.0, row_height=3.5, font_size=32,
                     header_color='#40466e', row_colors=['#f5f5f5', 'w'], edge_color='black',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (array(data.shape[::-1]) + array([0, 1])) * array([col_width, row_height])
        fig, ax = subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax


def Main():
    # ##### Starting Execution Timer

    start_time = perf_counter()

    # ### Fetching Data from ERP

    url = config.URL

    try:
        driver = webdriver.Firefox()
    except:
        driver = webdriver.Chrome()

    driver.get(url)

    with open("creds.txt") as fi:
        l = list(map(lambda x: x.strip("\n"), fi.readlines()))
        UNAME = l[0]
        PASS = l[1]

    u = driver.find_element_by_name(config.UNAME_ID)
    u.send_keys(UNAME)
    p = driver.find_element_by_name(config.PASS_ID)
    p.send_keys(PASS)
    p.send_keys(Keys.RETURN)
    sleep(3)

    try:
        attendance = driver.find_element_by_id("aAttandance")
    except:
        sleep(3)
        attendance = driver.find_element_by_id("aAttandance")

    attendance.click()

    table = driver.find_element_by_class_name("table100")
    # head = table.find_element_by_tag_name("thead")
    body = table.find_element_by_tag_name("tbody")

    table_list = []
    for row in body.find_elements_by_tag_name("tr"):
        for col in row.find_elements_by_tag_name("td"):
            table_list.append(col.text)

    driver.close()

    # ### Processing Data

    table_list = list(filter(lambda x: (len(x) > 0) and (len(x) <= 4) and ("%" not in x), table_list))

    somelist = [i for j, i in enumerate(table_list) if j not in range(0,len(table_list), 5)]

    somelist = [i for j, i in enumerate(somelist) if j not in range(3, len(somelist), 4)]

    arr = array(list(map(int, somelist))).reshape(6, 3)[:, 1:]
    
    # ### Initializing Subjects

    total = {sub : [0 for i in range(config.N_ATTRIBUTES)] for sub in config.SUBJECTS}

    for sub, sub_arr in zip(total, arr):
        total[sub][1] = sub_arr[0]
        total[sub][2] = sub_arr[1]

    # ### Initializing Time Table

    tt = {
        config.MON : config.N_MON,
        config.TUE : config.N_TUE,
        config.WED : config.N_WED,
        config.THU : config.N_THU,
        config.FRI : config.N_FRI
    }

    x = [fun(i, tt[i], total) for i in tt]

    # ### Converting to Pandas DataFrame

    df = DataFrame(total, index=config.ATTRIBUTES)

    df = df.T

    df = df.reset_index()

    df.rename(columns={"index" : "Subjects"}, inplace=True)

    # ### Calculating Attendance

    df["Attendance(%)"] = (df["Present"] / (df["Present"] + df["Absent"])) * 100

    # ### Setting Attendence Threshold

    thresh = config.THRESHOLD

    # ### Calculating Bunks

    df["Bunks Left"] = floor((thresh * df["Total"]) - (df["Absent"]))

    df["Total Bunks"] = floor((thresh * df["Total"]))

    # ##### Displaying Code Execution Time

    att = df.plot.bar(x="Subjects", y="Attendance(%)", figsize=(10, 6))
    for p in att.patches:
        att.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')
    att.get_figure().savefig("MyAttendance.png", dpi=100)

    bks = df.plot.bar(x="Subjects", y="Bunks Left", figsize=(10, 6))
    for q in bks.patches:
        bks.annotate(format(q.get_height(), '.2f'), (q.get_x() + q.get_width() / 2., q.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')
    bks.get_figure().savefig("MyBunks.png", dpi=100)
    
    render_mpl_table(df, header_columns=1, col_width=7).get_figure().savefig("AttendanceDetails.png", dpi=30)

    end_time = perf_counter() - start_time
    print("Automation executed in", end_time, "seconds")


def fun(l, c, total):
    for i in range(c):
        for j in l:
            total[j][0] += 1
    return None


