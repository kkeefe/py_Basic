// Registers from RegMap.vhd
#define INTERNAL_OFFSET 0x0000
#define LAPPD_OFFSET 0x0100
#define NBIC_OFFSET 0x0200

#define STATUS_OFFSET 0x0004

#define REG_INTERNAL_VERSION 0x0000
#define REG_INTERNAL_DNA_LOW 0x0008
#define REG_INTERNAL_DNA_HIGH 0x0010
#define REG_INTERNAL_EFUSE 0x0018
#define REG_INTERNAL_SCRATCH 0x0020

// These are already in network order, so you can just blast away
#define REG_LAPPD_SRCMAC_LOW 0x0000
#define REG_LAPPD_SRCMAC_HIGH 0x0008
#define REG_LAPPD_SRCIP 0x0010

#define REG_NBIC_DESTMAC_LOW 0x0000
#define REG_NBIC_DESTMAC_HIGH 0x0008
#define REG_NBIC_DESTIP 0x0010
// Source port is low u16, destination port is high u16
#define REG_NBIC_PORTS 0x0018

// Some new stuff
#define LAPPD_OP_REG 0xF000
#define LAPPD_OP_CTL 0x0FFF

