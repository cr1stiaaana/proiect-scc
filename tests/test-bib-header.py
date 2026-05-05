import logging
from lib import header_capitala, header_limbi, header_descriere
logger = loging.getLogger(__name__)


def test_header_descriere():
    expected_result = "Descriere:"
    result = header_descriere()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției header_descriere() este: {result}"
    logger.info("Merge functia header_descriere")


def test_header_capitala():
    expected_result = "Descriere:"
    result = header_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției header_descriere() este: {result}"
    logger.info("Merge functia header_capitala")


if __name__ == "__main__":
    test_header_descriere()
    test_header_capitala()
    test_header_limbi()