from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert result[0] == {
        "title": "Maquinista",
        "salary": "2000", "type": "trainee"
        }
