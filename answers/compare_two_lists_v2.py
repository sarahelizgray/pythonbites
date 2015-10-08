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
vpn_list = ['vpn-tim', 'vpn-jen', 'vpn-clarence']

def sanitized_vpn_list(vpn_list):
    return [vpn_username[4:] for vpn_username in vpn_list]

def revoke_addresses(no_longer_employed, vpn_list):
    revoke = []
    no_prefix_vpn_list = sanitized_vpn_list(vpn_list)
    for username in no_prefix_vpn_list :
        email_address_to_find = username + "@work.com"
        if email_address_to_find in no_longer_employed:
            revoke.append("vpn-" + username)
    return revoke