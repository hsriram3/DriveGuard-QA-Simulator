#include <stdio.h>
// firmware logic
//like ELD device code
int main() {
    int speed = 74;
    float odometer = 15023.4;
    printf("Firmware Log:\n");
    printf("Speed: %d mph\n", speed);
    printf("Odometer: %.1f miles\n", odometer);
    return 0;
}