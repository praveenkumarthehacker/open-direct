import requests
from urllib.parse import urlparse, parse_qs, urljoin

# List of common query parameters used for redirection
COMMON_REDIRECT_PARAMETERS = ['url', 'redirect', 'next', 'goto']

def scan_url_for_open_redirect(url):
    try:
        response = requests.get(url, allow_redirects=True)
        final_url = response.url
        
        # Check if the final URL is different from the original URL
        if final_url != url:
            # Parse the original URL and the final URL
            parsed_original = urlparse(url)
            parsed_final = urlparse(final_url)
            
            # Check if the original and final URLs are different domains
            if parsed_original.netloc != parsed_final.netloc:
                return f"Possible open redirect vulnerability detected: {url} -> {final_url}"
            
            # Check query parameters for potential redirect parameters
            query_params = parse_qs(parsed_original.query)
            for param in COMMON_REDIRECT_PARAMETERS:
                if param in query_params:
                    redirect_target = query_params[param][0]
                    # Check if the redirect target is an external URL
                    if urlparse(redirect_target).netloc:
                        return f"Possible open redirect vulnerability detected via parameter '{param}': {url} -> {final_url}"
        
        return f"No open redirect detected for: {url}"
    except requests.exceptions.RequestException as e:
        return f"Error scanning {url}: {e}"

