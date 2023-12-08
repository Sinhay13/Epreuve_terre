/*
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle.


*/

package main

import "fmt"

// stock alphabet in variable
var alphabet = [26]string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
	"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

// Print alphabet
func main() {
	for letters := range alphabet {
		fmt.Println(alphabet[letters])
	}
}
