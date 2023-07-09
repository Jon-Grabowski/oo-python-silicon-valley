from lib import *

# code here
# e.g.
su1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
su2 = Startup( 'Fight Milk', 'Mac', 'www.fightmilk.com' )
su3 = Startup( 'Kitten Mittens', 'Charlie', 'www.kittenmittens.com' )
su4 = Startup( 'Wolf Cola', 'Frank', 'www.wolfcola.com' )


vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
vc2 = VentureCapitalist( 'Russ Hanniman', 1000000000 )


fr1 = FundingRound( su1, vc1, 'Pre-Seed', 200000.99 )
fr2 = FundingRound( su1, vc2, 'Pre-Seed', 500000 )
fr3 = FundingRound( su2, vc2, 'Pre-Seed', 800000 )
fr4 = FundingRound( su1, vc1, 'Series-B', 400000.01 )







# do not remove
import ipdb; ipdb.set_trace()
