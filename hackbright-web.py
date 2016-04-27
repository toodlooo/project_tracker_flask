from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
	"""Show form for searching for a student."""

	return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
    						first=first,
    						last=last,
    						github=github)
    return html


@app.route("/student-add")
def student_add():
	"""Add a student."""

	return render_template("student_add.html")


@app.route("/student-confirmation", methods=['POST'])
def add_student_info():
	"""Add a student."""

	firstname = request.form.get('first_name')
	lastname = request.form.get('last_name')
	github = request.form.get('github')
	hackbright.make_new_student(firstname, lastname, github)
	html = render_template("student_confirmation.html",
    						firstname=firstname,
    						lastname=lastname,
    						github=github)

	return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
