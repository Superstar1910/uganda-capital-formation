"""Funding identities; do not equate financing with national capital formation."""
def reconcile(sources, new_capex, refinancing, other_uses=0):
    if not sources or any(v<0 for v in sources.values()) or min(new_capex,refinancing,other_uses)<0:
        raise ValueError("Nonnegative sources and uses required")
    funded=sum(sources.values());uses=new_capex+refinancing+other_uses
    if abs(funded-uses)>1e-8:raise ValueError("Sources and uses do not balance")
    return {'total_financing':funded,'new_productive_capex':new_capex,'refinancing':refinancing,'investor_shares':dict(sources)}
