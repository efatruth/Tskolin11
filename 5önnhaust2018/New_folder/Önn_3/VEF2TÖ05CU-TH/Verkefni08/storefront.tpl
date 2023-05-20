<!DOCTYPE html>
<html>
	<head>
		<title>Store</title>
	</head>
	<body>
	<h2> Spurningar í Verk.8 </h2>
	<p>
    Q. Hvað er session?:
        Sessions eru geymslur af upplýsingum sem er kallað á, á meðan notandinn er að nota síðu.

    Q. Hver er munurinn á sessions og cookies?:
        Cookies eru hluti af gögnum sem eru geymd af vafranum sem verða svo sent til serversins þegar það er boðið um,
        session er safn af gögnum sem serverinn heldur utan um.

    C. Session ID (cookie) og hvernig það tengist sessions á miðlara?:
        Session ID er einstakt númer serverinn á síðunni gefur hverjum notanda á meðan notandinn er í síðunni.
        Í hvert skipti sem notandi fer á síðu, fær hann nýtt session ID.
    </p>

	    <h2>Vörur</h2>
		<form method="post", action="/">
			<input type="checkbox" name="Roll" value="Paper Roll" {{"checked" if 'Roll' in count else ''}} id="vara1"/>Paper Roll
			<br>
			<input type="checkbox" name="Wash" value="Body Wash" {{"checked" if 'Wash' in count else ''}} id="vara2"/>Body Wash
            <br>
			<input type="checkbox" name="Towel" value="Body Towel" {{"checked" if 'Towel' in count else ''}} id="vara3"/>Body Towel
            <br>
			<input type="checkbox" name="Shampoo" value="Shampoo" {{"checked" if 'Shampoo' in count else ''}} id="vara4"/>Shampoo
            <br>
            <br>
			<input type="submit" name="submit" value="Kerra">
		</form>
		<p> Þú hefur komið í þessa síðu {{visit}} sinnum. </p>

	</body>
</html>