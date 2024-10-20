import logging, platform
from enum import Enum

logger = logging.getLogger(__name__)

class OSValidator:
    """Single utility class for operating system validation.

    Example usage:
        result, message = OSValidator.validate(OSValidator.OSValidatorEnum.WINDOWS)
        if not result:
            logger.error(message)
    """

    class OSValidationStatusEnum(Enum):
        """Validation status enum"""
        SUCCESS = True
        FAILURE = False

    class OSValidatorEnum(Enum):
        """Operating system types for validation."""
        WINDOWS = 0
        LINUX = 1
        MAC = 2

    # Mapping OSValidatorEnum to sets of system OS strings
    __OS_MAP = {
        OSValidatorEnum.WINDOWS: {"Windows", "win32", "cygwin"},
        OSValidatorEnum.LINUX: {"Linux", "linux"},
        OSValidatorEnum.MAC: {"Darwin", "macOS", "Mac OS X"}
    }

    @staticmethod
    def validate(expected_os_enum: 'OSValidator.OSValidatorEnum') -> tuple[bool, str]:
        """Validate the system operating system against the expected OS and return status and message."""
        current_os = platform.system()

        # Check if the expected_os_enum exists in the OS_MAP dictionary
        if expected_os_enum not in OSValidator.__OS_MAP:
            return False, f"Unknown operating system: {expected_os_enum}"

        # Validate if the current OS matches the expected OS
        if current_os in OSValidator.__OS_MAP[expected_os_enum]:
            return True, "Operating system validated."
        
        return False, f"Expected OS: '{expected_os_enum.name}', but found: '{current_os}'"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)
    logger.info("Running os validator independently...")

    result, message = OSValidator.validate(OSValidator.OSValidatorEnum.WINDOWS)
    if not result:
        logger.info(message)