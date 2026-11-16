
from sklearn.model_selection import train_test_split

# Mage supplies decorators when executing a Mage pipeline.
# The fallback allows this block to be imported by normal Python and pytest.
try:
    from mage_ai.data_preparation.decorators import transformer
except ImportError:
    def transformer(func):
        return func


TEST_SIZE = 0.3
RANDOM_STATE = 42


@transformer
def transform(df, *args, **kwargs):
    """
    Add a deterministic train/test split to the Iris DataFrame.

    Expected input: 150 rows containing the Iris features and target.
    Expected output: 120 train rows and 30 test rows.
    """
    if "target" not in df.columns:
        raise ValueError("Input DataFrame must contain a 'target' column.")

    if df.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    train_indices, test_indices = train_test_split(
        df.index,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=df["target"],
    )

    result = df.copy()
    result["split"] = "train"
    result.loc[test_indices, "split"] = "test"

    return result
