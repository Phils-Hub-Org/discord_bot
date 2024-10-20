import logging, platform
from enum import Enum

logger = logging.getLogger(__name__)

class ArchValidator:
    """Single utility class for architecture validation.

    Example usage:
        result, message = ArchValidator.validate(ArchValidator.ArchValidatorEnum.X64)
        if not result:
            logger.error(message)
    """

    class ArchValidationStatusEnum(Enum):
        """Validation status enum"""
        SUCCESS = True
        FAILURE = False

    class ArchValidatorEnum(Enum):
        """Architecture types for validation."""
        X86 = 0
        X64 = 1

    # Mapping architecture strings to enum
    __ARCH_MAP = {
        ArchValidatorEnum.X86: {"32", "x86", "i386", "i686", "arm", "armhf"},
        ArchValidatorEnum.X64: {"64", "amd64", "x64", "x86_64", "arm64", "aarch64", "ppc64le", "s390x", "mips64", "riscv64"}
    }

    @staticmethod
    def validate(expected_arch_enum: 'ArchValidator.ArchValidatorEnum') -> tuple[bool, str]:
        """Validate the system architecture against expected architecture and return status and message."""
        current_arch = platform.machine()

        # Check if the expected_arch_enum exists in the ARCH_MAP dictionary
        if expected_arch_enum not in ArchValidator.__ARCH_MAP:
            return False, f"Unknown architecture: {expected_arch_enum}"

        # Validate if the current architecture matches the expected architecture
        if current_arch.lower() in ArchValidator.__ARCH_MAP[expected_arch_enum]:
            return True, "Architecture validated."
        
        return False, f"Expected architecture: '{expected_arch_enum.name}', but found: '{current_arch}'"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    logger.info("Loading arch validator independently...")

    result, message = ArchValidator.validate(ArchValidator.ArchValidatorEnum.X64)
    if not result:
        logger.info(message)