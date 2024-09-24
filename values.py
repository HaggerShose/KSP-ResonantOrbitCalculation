"""/*

Configuration data for the Resonant Orbit Calculator v1.3 (https://meyerweb.com/eric/ksp/resonant-orbits/).

The following are REQUIRED for each body:
	"color":  "six-digit hexadecimal RGB value" (e.g. white = #FFFFFF), MUST be quoted
	"mass":   mass, in kilograms (E+ notation preferred but not required)
	"eqr":    equatorial radius, in meters
	"day":    rotational period (i.e., length of a day), in seconds; use negative for retrograde spin (e.g., Venus)
	"atm":    outer edge of the atmosphere, in meters; use 0 if there is no atmosphere
	"SOI":    the sphere of influence radius, in meters; use 1E+15 or higher for the system's central sun

The color values were chosen based on the in-game appearance of each planet, NOT the orbit color in Map view.


You can add other properties if you feel like it, but they'll be ignored.

*/"""

systems = {
    "KSP Stock": {
        "Kerbol": {
            "color": "#FE9",
            "mass": 1.7565459e28,
            "eqr": 261600000,
            "day": 432000,
            "atm": 600000,
            "SOI": 1e15,
        },
        "Moho": {
            "color": "#80736B",
            "mass": 2.52633139930162e21,
            "eqr": 250000,
            "day": 1210000,
            "atm": 0,
            "SOI": 9646663.02332811,
        },
        "Eve": {
            "color": "#897695",
            "mass": 1.2243980038014e23,
            "eqr": 700000,
            "day": 80500,
            "atm": 90000,
            "SOI": 85109364.7382441,
        },
        "Gilly": {
            "color": "#867D78",
            "mass": 1.24203632781093e17,
            "eqr": 13000,
            "day": 28255,
            "atm": 0,
            "SOI": 126123.271704568,
        },
        "Kerbin": {
            "default": True,
            "color": "#495B66",
            "mass": 5.29151583439215e22,
            "eqr": 600000,
            "day": 21549.4251830898,
            "atm": 70000,
            "SOI": 84159286.4796305,
        },
        "Mun": {
            "color": "#888",
            "mass": 9.7599066119646e20,
            "eqr": 200000,
            "day": 138984.376574476,
            "atm": 0,
            "SOI": 2429559.11656475,
        },
        "Minmus": {
            "color": "#9BB4A5",
            "mass": 2.64575795662095e19,
            "eqr": 60000,
            "day": 40400,
            "atm": 0,
            "SOI": 2247428.3879023,
        },
        "Duna": {
            "color": "#905646",
            "mass": 4.51542702477492e21,
            "eqr": 320000,
            "day": 65517.859375,
            "atm": 50000,
            "SOI": 47921949.369738,
        },
        "Ike": {
            "color": "#888",
            "mass": 2.78216152235874e20,
            "eqr": 130000,
            "day": 65517.8621348081,
            "atm": 0,
            "SOI": 1049598.93931162,
        },
        "Dres": {
            "color": "#878482",
            "mass": 3.21909365785247e20,
            "eqr": 138000,
            "day": 34800,
            "atm": 0,
            "SOI": 32832839.5767762,
        },
        "Jool": {
            "color": "#708D4B",
            "mass": 4.23321273059351e24,
            "eqr": 6000000,
            "day": 36000,
            "atm": 200000,
            "SOI": 2455985185.42347,
        },
        "Laythe": {
            "color": "#5C6068",
            "mass": 2.93973106291216e22,
            "eqr": 500000,
            "day": 52980.8790593796,
            "atm": 50000,
            "SOI": 3723645.81113302,
        },
        "Vall": {
            "color": "#879192",
            "mass": 3.10876554482042e21,
            "eqr": 300000,
            "day": 105962.088893924,
            "atm": 0,
            "SOI": 2406401.44479404,
        },
        "Tylo": {
            "color": "#9B9894",
            "mass": 4.23321273059351e22,
            "eqr": 600000,
            "day": 211926.35802123,
            "atm": 0,
            "SOI": 10856518.3683586,
        },
        "Bop": {
            "color": "#655D57",
            "mass": 3.72610898343278e19,
            "eqr": 65000,
            "day": 544507.428516654,
            "atm": 0,
            "SOI": 1221060.86284253,
        },
        "Pol": {
            "color": "#938C7E",
            "mass": 1.08135065806823e19,
            "eqr": 44000,
            "day": 901902.623531173,
            "atm": 0,
            "SOI": 1042138.89230178,
        },
        "Eeloo": {
            "color": "#959B9B",
            "mass": 1.1149224e21,
            "eqr": 210000,
            "day": 19460,
            "atm": 0,
            "SOI": 119082941.6,
        },
    },
}
