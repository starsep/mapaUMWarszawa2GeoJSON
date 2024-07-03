from utils import formatFileSize


def test_formatFileSize():
    assert formatFileSize(123) == "123B"
    assert formatFileSize(12345) == "12.06kB"
    assert formatFileSize(123456789) == "117.74MB"
