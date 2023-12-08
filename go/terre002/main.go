/*
Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.


Exemples d’utilisation :
$> ruby exo.rb je suis solide !
je
suis
solide
!

*/

package main

import (
	"fmt"
	"os"
)

func capture() []string {
	args := os.Args[1:]
	return args

}

func printLoop(a []string) {
	for item := range len(a) {
		fmt.Println(a[item])
	}
}

func main() {
	args := capture()
	printLoop(args)
}

// to work on !
