from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','groundstation0'),('instrument1','star3'),('instrument10','star3'),('instrument11','star1'),('instrument12','groundstation0'),('instrument13','star1'),('instrument14','groundstation2'),('instrument15','groundstation4'),('instrument16','star1'),('instrument17','groundstation0'),('instrument18','star1'),('instrument19','groundstation4'),('instrument2','groundstation0'),('instrument20','star1'),('instrument21','star1'),('instrument22','groundstation0'),('instrument23','star3'),('instrument3','groundstation4'),('instrument4','groundstation2'),('instrument5','groundstation4'),('instrument6','groundstation2'),('instrument7','groundstation0'),('instrument8','groundstation4'),('instrument9','star1')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite1'),('instrument10','satellite4'),('instrument11','satellite5'),('instrument12','satellite6'),('instrument13','satellite6'),('instrument14','satellite6'),('instrument15','satellite7'),('instrument16','satellite8'),('instrument17','satellite8'),('instrument18','satellite9'),('instrument19','satellite9'),('instrument2','satellite1'),('instrument20','satellite10'),('instrument21','satellite10'),('instrument22','satellite10'),('instrument23','satellite11'),('instrument3','satellite2'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite3'),('instrument7','satellite3'),('instrument8','satellite3'),('instrument9','satellite4')])
state.pointing = Oset([('satellite0','planet5'),('satellite1','planet5'),('satellite10','star22'),('satellite11','star8'),('satellite2','star21'),('satellite3','star21'),('satellite4','star22'),('satellite5','groundstation2'),('satellite6','phenomenon20'),('satellite7','planet12'),('satellite8','phenomenon23'),('satellite9','phenomenon20')])
state.power_avail = Oset(['satellite0','satellite1','satellite10','satellite11','satellite2','satellite3','satellite4','satellite5','satellite6','satellite7','satellite8','satellite9'])
state.supports = Oset([('instrument0','infrared3'),('instrument1','image0'),('instrument1','infrared2'),('instrument10','image0'),('instrument10','image4'),('instrument11','infrared2'),('instrument12','image4'),('instrument13','image4'),('instrument14','infrared2'),('instrument14','thermograph1'),('instrument15','image0'),('instrument15','thermograph1'),('instrument16','image0'),('instrument16','infrared2'),('instrument17','infrared3'),('instrument18','image4'),('instrument18','infrared2'),('instrument18','thermograph1'),('instrument19','infrared3'),('instrument2','image0'),('instrument2','thermograph1'),('instrument20','infrared2'),('instrument21','image0'),('instrument21','thermograph1'),('instrument22','thermograph1'),('instrument23','image4'),('instrument23','infrared2'),('instrument23','thermograph1'),('instrument3','infrared2'),('instrument3','infrared3'),('instrument4','infrared2'),('instrument4','infrared3'),('instrument4','thermograph1'),('instrument5','thermograph1'),('instrument6','image0'),('instrument6','infrared2'),('instrument7','image0'),('instrument7','infrared3'),('instrument8','image0'),('instrument8','image4'),('instrument8','infrared2'),('instrument9','infrared3')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon14','infrared2'),('phenomenon15','infrared2'),('phenomenon17','thermograph1'),('phenomenon23','infrared3'),('phenomenon24','infrared3'),('phenomenon9','image4'),('planet11','image4'),('planet12','thermograph1'),('planet13','infrared3'),('planet16','infrared2'),('planet5','image0'),('planet6','image4'),('planet7','image4'),('star10','thermograph1'),('star18','image4'),('star21','thermograph1'),('star22','image4')])
goals.pointing = Oset([('satellite1','star22'),('satellite4','phenomenon20'),('satellite8','planet16')])

