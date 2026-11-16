from config.settings import OWNER_NAME, ROLL_NUMBER, PROJECT_NAME

def test_project_identity():
    assert OWNER_NAME == "Shikhar Pandey"
    assert ROLL_NUMBER == "26pcso05"
    assert PROJECT_NAME == "FreshCart – From Git to Gold"
