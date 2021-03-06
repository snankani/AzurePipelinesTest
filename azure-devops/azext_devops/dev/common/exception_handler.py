# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)


def azure_devops_exception_handler(ex):
    # we are taking dependency on string here because taking dependency on
    # Azure DevOps Client will increase load time for every command
    if type(ex).__name__ == 'VstsServiceError':
        logger.debug('handling vsts service error')
        raise CLIError(ex)
    else:
        logger.debug('handling generic error')
        import sys
        from six import reraise
        reraise(*sys.exc_info())
