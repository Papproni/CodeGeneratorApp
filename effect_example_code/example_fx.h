/*
This is an example code for template for the Code Generator GUI
*/

#include "stdint.h"


/* REQUIREMENT ONE:
Create the internal varables for the effect and place it in a struct 
*/
typedef struct {
    float 		delay_time; 					// in ms
    uint32_t 	time_in_buffer_u32; 		// in buffer location 1 = 1/48 ms
    uint32_t 	modulation_in_buffer_u32;	// sets the modulation of the delay
    uint32_t	modulation_counter_u32;
    int32_t		modulation_amplitude_i32;
    uint32_t 	modulation_base_u32;
    float 		mix_f32;  					// delay and input
    uint8_t 	repeats_u8;					// number of repeats
    float   	feedback_gain_f32;			// how repeats weaken over time
} TEMPLATE_effect_tst;

void init_TEMPLATE(void* effect);
void process_TEMPLATE(void* effect);


