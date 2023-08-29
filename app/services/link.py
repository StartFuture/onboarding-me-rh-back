import uuid
import time
from urllib.parse import urlencode,urlparse, parse_qs

class Link:

    @staticmethod
    def create_expiring_link(base_url: str = 'https://example.com/') -> str:

        token = str(uuid.uuid4())
        two_days: int = 172800
        expiration_time = time.time() + two_days

        link_data = {
            'token': token,
            'expiration_time': expiration_time
        }

        query_string = urlencode(link_data)
        expiring_link = f'{base_url}?{query_string}'

        return expiring_link

    @staticmethod
    def is_link_valid(link: str) -> bool:
        
        parsed_url = urlparse(link)
        query_params = parse_qs(parsed_url.query)

        if 'token' in query_params and 'expiration_time' in query_params:
            token = query_params['token'][0]
            expiration_time = float(query_params['expiration_time'][0])

            current_time = time.time()

            if current_time <= expiration_time:
                return True
            else:
                return False 
        else:
            return False 
