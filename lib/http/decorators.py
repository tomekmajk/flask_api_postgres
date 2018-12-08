from lib.token.token_manager import valid_token

def api_endpoint(auth_required=True, permissions=[]):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            request = args[0]
            if auth_required:
                print('auth token check from headers')
            for has_perm in permissions:
                print('has perm?', has_perm())
            return f(*args, **kwargs)
        return wrapped_f
    return wrap
