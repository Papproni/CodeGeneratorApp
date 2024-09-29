/*THIS FILE IS GENERATED! DO NOT MODIFY!
Generated on: 2024.09.29. */

#ifndef SAB__H
#define SAB__H


#include "stdint.h"

// Generated effect libs
#include "SAB_delay.h"
#include "SAB_overdrive.h"
#include "SAB_distortion.h"
#include "SAB_octave.h"

#define float32_t float


// Manager structure: 
typedef struct {
} SAB__tst;


// Process Function for SAB__tst
int SAB__init( SAB__tst* self, float input_f32, float output_f32);

// Process Function for SAB__tst
int SAB__process( SAB__tst* self, float input_f32, float output_f32);



#endif