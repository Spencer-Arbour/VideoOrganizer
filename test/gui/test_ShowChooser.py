import pytest

from gui.ShowChooser import ShowChooser


class TestShowChooser:
    _TWO_HUNDRED_LETTERS = (
            "ASzbN1pPMiCoKCsnklCYrjNkjXStYUW6PKQz3Lw9"
            "I1sZ3mVfkdAIS59bIK6Nk8TUEhEOaMnCxsFHkZe4"
            "iMJfS3r1FlynQFuEmIjBhGkCrOk4750fo0XeKuXy"
            "HMgTy14kBcOawO2gKK27y274XwYFHc7AMUE0c89B"
            "bDbWNYzVH13vTYqMbAytX26aMuCisix9VqDqXDf0"
    )

    _ONE_HUNDRED_TWENTY_THREE_LETTERS = (
        "ASzbN1pPMiCoKCsnklCYrjNkjXStYUW6PKQz3Lw9"
        "I1sZ3mVfkdAIS59bIK6Nk8TUEhEOaMnCxsFHkZe4"
        "iMJfS3r1FlynQFuEmIjBhGkCrOk4750fo0XeKuXy"
        "HMg"
    )

    @pytest.mark.regression
    @pytest.mark.parametrize("in_put, expected", [
        (_TWO_HUNDRED_LETTERS, _TWO_HUNDRED_LETTERS),
        (_TWO_HUNDRED_LETTERS + "p", _TWO_HUNDRED_LETTERS[:-3] + "...")
    ])
    def test_if_no_trim_len_supplied_200_default_used(self, in_put, expected):
        ans = ShowChooser._trim_overview(in_put)
        assert ans == expected

    @pytest.mark.regression
    @pytest.mark.parametrize("trim_len", [0, -1])
    @pytest.mark.parametrize("in_put, expected", [
        (_TWO_HUNDRED_LETTERS, _TWO_HUNDRED_LETTERS),
        (_TWO_HUNDRED_LETTERS + "p", _TWO_HUNDRED_LETTERS[:-3] + "...")
    ])
    def test_zero_less_trim_len_uses_200_default(self, trim_len, in_put, expected):
        ans = ShowChooser._trim_overview(in_put, trim_len)
        assert ans == expected

    @pytest.mark.regression
    @pytest.mark.parametrize("in_put, expected", [
        (_ONE_HUNDRED_TWENTY_THREE_LETTERS, _ONE_HUNDRED_TWENTY_THREE_LETTERS),
        (_ONE_HUNDRED_TWENTY_THREE_LETTERS + "p", _ONE_HUNDRED_TWENTY_THREE_LETTERS[:-3] + "...")
    ])
    def test_trim_len_used_if_overview_longer(self, in_put, expected):
        ans = ShowChooser._trim_overview(in_put, len(self._ONE_HUNDRED_TWENTY_THREE_LETTERS))
        assert ans == expected
