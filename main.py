# Student Grade Calculator 

from pyscript import document, display

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

    summary = f"""
    <h4>Name: {first_name} {last_name}</h4>
    <br>
    {subjects[0]}: {grades[0]}<br>
    {subjects[1]}: {grades[1]}<br>
    {subjects[2]}: {grades[2]}<br>
    {subjects[3]}: {grades[3]}<br>
    {subjects[4]}: {grades[4]}<br>
    {subjects[5]}: {grades[5]}<br><br>
    <strong>Your general weighted average is: {gwa:.2f}</strong>
    """

    output_div = document.getElementById("output")
    output_div.innerHTML = summary