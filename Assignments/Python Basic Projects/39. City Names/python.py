def describe_city(city: str, country: str) -> str:
    return f'"{city}, {country}"'


print(describe_city('Karachi', 'Pakistan'))
print(describe_city('London', 'British'))
print(describe_city('California', 'America'))
