# Copyright 2015 Rackspace, Inc.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
No-op network provider. Useful for shared, flat networks.
"""

from ironic.networks import base


class NoopNetworkProvider(base.NetworkProvider):
    """No-op network provider."""

    def add_provisioning_network(self, task):
        """Add the provisioning network to a node.

        :param task: A TaskManager instance.
        """
        pass

    def remove_provisioning_network(self, task):
        """Remove the provisioning network from a node.

        :param task: A TaskManager instance.
        """
        pass

    def configure_tenant_networks(self, task):
        """Configure tenant networks for a node.

        :param task: A TaskManager instance.
        """
        pass

    def unconfigure_tenant_networks(self, task):
        """Unconfigure tenant networks for a node.

        :param task: A TaskManager instance.
        """
        pass

    def add_cleaning_network(self, task):
        """Add the cleaning network to a node.

        :param task: A TaskManager instance.
        :returns: a dictionary in the form {port.uuid: neutron_port['id']}
        """
        pass

    def remove_cleaning_network(self, task):
        """Remove the cleaning network from a node.

        :param task: A TaskManager instance.
        """
        pass