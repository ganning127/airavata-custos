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

package org.apache.custos.tenant.profile.client.async;

import io.grpc.ClientInterceptor;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.stub.StreamObserver;
import org.apache.custos.integration.core.ServiceCallback;
import org.apache.custos.integration.core.ServiceException;
import org.apache.custos.tenant.profile.service.AddTenantResponse;
import org.apache.custos.tenant.profile.service.Tenant;
import org.apache.custos.tenant.profile.service.TenantProfileServiceGrpc;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * This class uses gRPC stubs generated for {@link TenantProfileServiceGrpc}
 * and acts as the client
 */
@Component
public class TenantProfileClient {

    private ManagedChannel managedChannel;
    private TenantProfileServiceGrpc.TenantProfileServiceStub profileServiceStub;
    private TenantProfileServiceGrpc.TenantProfileServiceBlockingStub profileServiceBlockingStub;


    private final List<ClientInterceptor> clientInterceptorList;


    public TenantProfileClient(List<ClientInterceptor> clientInterceptorList,
                               @Value("${tenant.profile.core.service.dns.name}")  String serviceHost,
                                        @Value("${tenant.profile.core.service.port}") int servicePort) {
        this.clientInterceptorList = clientInterceptorList;
        managedChannel = ManagedChannelBuilder.forAddress(
                serviceHost, servicePort).usePlaintext(true).intercept(clientInterceptorList).build();
        profileServiceStub = TenantProfileServiceGrpc.newStub(managedChannel);
        profileServiceBlockingStub = TenantProfileServiceGrpc.newBlockingStub(managedChannel);
    }

    public void addTenantAsync(Tenant tenant, final ServiceCallback callback) {

        final AddTenantResponse[] response = new AddTenantResponse[1];

        StreamObserver observer = new StreamObserver() {
            @Override
            public void onNext(Object o) {
               response[0] = ((AddTenantResponse)o);
            }

            @Override
            public void onError(Throwable throwable) {
                callback.onCompleted(null, new ServiceException("Add tenant task failed", throwable, null));
            }

            @Override
            public void onCompleted() {
                callback.onCompleted(response[0], null);
            }
        };


        profileServiceStub.addTenant(tenant, observer);
    }


    public AddTenantResponse addTenant(Tenant tenant) {
        AddTenantResponse response = profileServiceBlockingStub.addTenant(tenant);
        return response;

    }


}
