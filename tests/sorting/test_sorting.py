from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
       {
        "job_title": "Data Scientist",
        "min_salary": "112157",
        "max_salary": "149698",
        "date_posted": "2020-05-02"
        }, {
        "job_title": "Associate Director",
        "min_salary": "105899",
        "max_salary": "135899",
        "date_posted": "2020-06-05"
        }, {
        "job_title": "Full Stack Developer",
        "min_salary": "107899",
        "max_salary": "138899",
        "date_posted": "2020-04-04"
        }
    ]
    result = sort_by(jobs, "min_salary")
    assert result[0]["job_title"] == "Associate Director"
    assert result[2]["job_title"] == "Data Scientist"
