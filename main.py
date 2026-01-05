# Student Grade Calculator 

from pyscript import document

subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
units = (5, 5, 5, 3, 2, 1)

def calculate_gwa(e):
    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    grades = [
        float(document.getElementById("science").value),
        float(document.getElementById("math").value),
        float(document.getElementById("english").value),
        float(document.getElementById("filipino").value),
        float(document.getElementById("ict").value),
        float(document.getElementById("pe").value)
    ]

    total_units = sum(units)
    weighted_sum = sum(grades[i] * units[i] for i in range(len(subjects)))
    gwa = weighted_sum / total_units

    if gwa >= 75:
        status = "Passed"
    else:
        status = "Failed"
    summary = f"""
    <h4>Name: {first_name} {last_name}</h4>
    <br>
    Science: {grades[0]}<br>
    Math: {grades[1]}<br>
    English: {grades[2]}<br>
    Filipino: {grades[3]}<br>
    ICT: {grades[4]}<br>
    PE: {grades[5]}<br><br>
    <strong>GWA: {gwa:.2f}</strong><br>
    <strong>Status: {status}</strong>
    """

    document.getElementById("output").innerHTML = summary
