#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>


#define NUM_OF_FX_IN_LOOP 3

// Enum representing different effect types
typedef enum {
    BOOST,
    OVERDRIVE,
    DELAY,
    EFFECT_COUNT  // Keeps track of the number of effects
} EffectType;

typedef enum {
    FX_ACTIVE,
    FX_BYPASSED
} Effectstate_ten;

// Struct for a guitar effect with function pointers
typedef struct {
    EffectType type;
    Effectstate_ten state;
    void (*init)(void*);           // Function pointer to initialize the effect
    void (*copy_from_flash)(void*); // Function pointer to copy data from flash
    void (*process)(void*);         // Function pointer to process the effect
} GuitarEffect;

// BOOST effect structure and functions
typedef struct {
    int boost_level;
} BoostEffect;

void init_boost(void* effect) {
    BoostEffect* boost = (BoostEffect*)effect;
    boost->boost_level = 10;  // Initialize the boost effect
    printf("Boost initialized with level %d\n", boost->boost_level);
}

void copy_boost_from_flash(void* effect) {
    // Simulate copying from flash (just for demonstration)
    BoostEffect* boost = (BoostEffect*)effect;
    boost->boost_level = 12;
    printf("Boost data copied from flash, level set to %d\n", boost->boost_level);
}

void process_boost(void* effect) {
    BoostEffect* boost = (BoostEffect*)effect;
    printf("Processing Boost effect at level %d\n", boost->boost_level);
}

// OVERDRIVE effect structure and functions
typedef struct {
    int drive_level;
} OverdriveEffect;

void init_overdrive(void* effect) {
    OverdriveEffect* od = (OverdriveEffect*)effect;
    od->drive_level = 5;
    printf("Overdrive initialized with drive level %d\n", od->drive_level);
}

void copy_overdrive_from_flash(void* effect) {
    OverdriveEffect* od = (OverdriveEffect*)effect;
    od->drive_level = 7;
    printf("Overdrive data copied from flash, drive level set to %d\n", od->drive_level);
}

void process_overdrive(void* effect) {
    OverdriveEffect* od = (OverdriveEffect*)effect;
    printf("Processing Overdrive effect with drive level %d\n", od->drive_level);
}

// DELAY effect structure and functions
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
} DelayEffect;

void init_delay(void* effect) {
    DelayEffect* delay = (DelayEffect*)effect;
    delay->delay_time = 200;
    printf("Delay initialized with time %d ms\n", delay->delay_time);
}

void copy_delay_from_flash(void* effect) {
    DelayEffect* delay = (DelayEffect*)effect;
    delay->delay_time = 400;
    printf("Delay data copied from flash, time set to %d ms\n", delay->delay_time);
}

void process_delay(void* effect) {
    DelayEffect* delay = (DelayEffect*)effect;
    printf("Processing Delay effect with time %d ms\n", delay->delay_time);
}

// Function to initialize the guitar effects chain
void init_effect_chain(GuitarEffect** chain, EffectType* fx_chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        switch (fx_chain[i]) {
        case BOOST:
            chain[i] = (GuitarEffect*)malloc(sizeof(BoostEffect));
            chain[i]->type = BOOST;
            chain[i]->init = init_boost;
            chain[i]->copy_from_flash = copy_boost_from_flash;
            chain[i]->process = process_boost;
            break;
        case OVERDRIVE:
            chain[i] = (GuitarEffect*)malloc(sizeof(OverdriveEffect));
            chain[i]->type = OVERDRIVE;
            chain[i]->init = init_overdrive;
            chain[i]->copy_from_flash = copy_overdrive_from_flash;
            chain[i]->process = process_overdrive;
            break;
        case DELAY:
            chain[i] = (GuitarEffect*)malloc(sizeof(DelayEffect));
            chain[i]->type = DELAY;
            chain[i]->init = init_delay;
            chain[i]->copy_from_flash = copy_delay_from_flash;
            chain[i]->process = process_delay;
            break;
        default:
            printf("Unknown effect type!\n");
            break;
        }
        // Initialize the effect
        chain[i]->init(chain[i]);
        // Copy data from flash (simulated)
        chain[i]->copy_from_flash(chain[i]);
    }
}

// Function to process all effects in the chain
void process_effect_chain(GuitarEffect** chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        if (FX_ACTIVE == chain[i]->state) {
            chain[i]->process(chain[i]);
        }
    }
}

// Cleanup the effects in the chain
void cleanup_effect_chain(GuitarEffect** chain, int chain_length) {
    for (int i = 0; i < chain_length; ++i) {
        free(chain[i]);  // Free the allocated memory for each effect
    }
}

int main() {
    // Define the effects chain sequence
    EffectType fx_chain[] = { BOOST, OVERDRIVE, DELAY };
    //int chain_length = sizeof(fx_chain) / sizeof(fx_chain[0]);

    // Create the chain array for storing the effect objects
    GuitarEffect* effect_chain[NUM_OF_FX_IN_LOOP];

    // Initialize the effect chain
    init_effect_chain(effect_chain, fx_chain, NUM_OF_FX_IN_LOOP);

    // Process the effect chain
    process_effect_chain(effect_chain, NUM_OF_FX_IN_LOOP);

    // Cleanup
    cleanup_effect_chain(effect_chain, NUM_OF_FX_IN_LOOP);

    return 0;
}
