from src.adapter.presenter import PaymentPresenter


def application_exception(func):
    def response(*args, **kwargs):
        try:
            response =  func(*args, **kwargs)
            return PaymentPresenter.success(response)
        except Exception as err:
            raise err
    return response
