import lxml.html

def get_machines():
    lvs = lxml.html.parse('http://laundryview.com/lvs.php')
    div = lvs.find(".//div[@id='campus1']")
    rooms = []
    status = []
    for a in div.findall('.//a'):
        rooms.append(str(a.text).strip().title())
    for span in div.findall('.//span'):
        status.append(str(span.text).strip())
    return dict(zip(rooms, status))

print get_machines()

