# I have two lists of names -- one list VPN usernames, 
# one list is all the email addresses of people who are no longer employed. 
# I want to write a script to tell me which VPN accounts to revoke 
# based on who is no longer employed.

# SAMPLE DATA
# LIST 1 -- Email Addresses of People Who are no longer employed
# bob@work.com
# suzie@work.com
# jen@work.com

# LIST 2 -- a complete list of VPN usernames
# vpn-tim
# vpn-jen
# vpn-clarence

# goal: revoke_vpn for vpn-jen

no_longer_employed = ['bob@work.com', 'suzie@work.com', 'jen@work.com']
vpn = ['vpn-tim', 'vpn-jen', 'vpn-clarence']

def sanitized_email(email_address) :
    return email_address.split('@')[0]

def revoke_addresses(no_longer_employed, vpn):
    revoke = []
    for email_address in no_longer_employed:
        username = sanitized_email(email_address)
        vpn_username = "vpn-" + username
        if vpn_username in vpn:
            revoke.append(vpn_username)
    return revoke