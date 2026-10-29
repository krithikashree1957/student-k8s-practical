from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<h1>Student Grade Calculator</h1>
<form method="post">
    <label>
        Marks (comma-separated):
        <input name="marks" placeholder="80,90,70" required>
    </label>
    <button type="submit">Calculate</button>
</form>
<p>{{ result }}</p>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        try:
            marks = [
                float(x.strip())
                for x in request.form["marks"].split(",")
                if x.strip()
            ]

            if not marks or any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError

            total = sum(marks)
            average = total / len(marks)
            result = f"Total: {total:g} | Average: {average:.2f}"

        except ValueError:
            result = "Enter valid marks between 0 and 100."

    return render_template_string(PAGE, result=result)


@app.get("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)