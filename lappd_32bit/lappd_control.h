// *this* version of lappdos protocol
#define LAPPD_VERSION_HARD 0xCafe
#define LAPPD_VERSION_SOFT 0x0002
#define LAPPD_VERSION_MASK_SOFT 0x0000FFFF
#define LAPPD_VERSION_MASK_HARD 0xFFFF0000

// Flag bits, shared by both register operations and anything else
#define LAPPD_OP_MASK_SILENT   0x0008   // 4-th bit position = 8
#define LAPPD_OP_MASK_FAILURE  0x0010   // 5-th bit position = 16

// Masks for register/other operations, flags preserving
#define LAPPD_OP_MASK_REG      0x001f  // bottom 5 bits
#define LAPPD_OP_MASK_OTHER    0xFFE0

// A null operation is reserved
#define LAPPD_READ 0x0001
#define LAPPD_WRITE 0x0002
#define LAPPD_STATUS 0x0003

// Things that we don't usually want to change
#define LAPPD_MAGIC_COOKIE 0x1337ca75
#define LAPPD_SERVER_PORT 1337
#define LAPPD_NBIC_PORT 1338
#define LAPPD_MAX_PAYLOAD 512

// Widths for register control protocol
#define LAPPD_WIDTH_REGISTER 4
#define LAPPD_WIDTH_OP 2
#define LAPPD_WIDTH_WIDTH 2
#define LAPPD_WIDTH_DATALEN 2
#define LAPPD_WIDTH_SEQNUM 4


