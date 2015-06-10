# -*- coding: utf-8 -*-
"""The arguments helper for the tagging analysis plugin."""

import os

from plaso.lib import errors
from plaso.cli.helpers import interface
from plaso.cli.helpers import manager
from plaso.analysis import tagging


class TaggingAnalysisHelper(interface.ArgumentsHelper):
  """CLI arguments helper class for the Tagging analysis plugin."""

  NAME = u'tagging'
  CATEGORY = u'analysis'
  DESCRIPTION = u'Argument helper for the Tagging analysis plugin.'

  @classmethod
  def AddArguments(cls, argument_group):
    """Add command line arguments the helper supports to an argument group.

    This function takes an argument parser or an argument group object and adds
    to it all the command line arguments this helper supports.

    Args:
      argument_group: the argparse group (instance of argparse._ArgumentGroup or
                      or argparse.ArgumentParser).
    """
    argument_group.add_argument(
        u'--tagging-file', dest=u'tagging_file', type=unicode,
        help=u'Specify a file to read tagging criteria from.',
        action=u'store')

  @classmethod
  def ParseOptions(cls, options, analysis_plugin):
    """Parses and validates options.

    Args:
      options: the parser option object (instance of argparse.Namespace).
      analysis_plugin: an analysis plugin (instance of OutputModule).

    Raises:
      BadConfigObject: when the output module object is of the wrong type.
      BadConfigOption: when a configuration parameter fails validation.
    """
    if not isinstance(analysis_plugin, tagging.TaggingPlugin):
      raise errors.BadConfigObject(
          u'Analysis plugin is not an instance of TaggingPlugin')

    tagging_file = getattr(options, u'tagging_file', None)
    if tagging_file:
      if not os.path.exists(tagging_file) or not os.path.isfile(tagging_file):
        raise errors.BadConfigOption(
            u'Tagging file {0:s} does not exist.'.format(tagging_file))
      analysis_plugin.SetAndLoadTagFile(tagging_file)


manager.ArgumentHelperManager.RegisterHelper(TaggingAnalysisHelper)