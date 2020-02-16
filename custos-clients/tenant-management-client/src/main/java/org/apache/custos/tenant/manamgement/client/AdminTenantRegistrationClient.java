/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 */

package org.apache.custos.tenant.manamgement.client;

import io.grpc.ManagedChannel;
import io.grpc.netty.GrpcSslContexts;
import io.grpc.netty.NettyChannelBuilder;
import org.apache.custos.clients.core.ClientUtils;
import org.apache.custos.tenant.management.service.CreateTenantResponse;
import org.apache.custos.tenant.management.service.TenantManagementServiceGrpc;
import org.apache.custos.tenant.profile.service.Tenant;

import javax.net.ssl.SSLException;

/**
 * The class used to register admin tenants
 */
public class AdminTenantRegistrationClient {

    private ManagedChannel managedChannel;

    private TenantManagementServiceGrpc.TenantManagementServiceBlockingStub blockingStubWithoutHeader;
    private TenantManagementServiceGrpc.TenantManagementServiceBlockingStub blockingStub;


    public AdminTenantRegistrationClient(String serviceHost, int servicePort, String certificateFilePath) throws SSLException {
        if (serviceHost == null || certificateFilePath == null) {
            throw new NullPointerException("Please provide all the parameters");
        }

        managedChannel = NettyChannelBuilder.forAddress(serviceHost, servicePort)
                .sslContext(GrpcSslContexts
                        .forClient()
                        .trustManager(ClientUtils.getFile(AdminTenantRegistrationClient.class, certificateFilePath)) // public key
                        .build())
                .build();


        blockingStubWithoutHeader = TenantManagementServiceGrpc.newBlockingStub(managedChannel);
    }


    /**
     * Registers Admin tenants
     *
     * @param tenant
     * @return {
     * string client_id
     * string client_secret
     * bool is_activated
     * double client_id_issued_at
     * double client_secret_expires_at
     * string registration_client_uri
     * string token_endpoint_auth_method
     * string msg = 7
     * }
     */
    public CreateTenantResponse createAdminTenant(Tenant tenant) {
        return blockingStubWithoutHeader.createTenant(tenant);
    }
}
